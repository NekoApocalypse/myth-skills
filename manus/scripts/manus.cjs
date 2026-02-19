const fs = require('fs');
const https = require('https');
const url = require('url');

const API_BASE = "https://api.manus.ai/v1";
const API_KEY = process.env.MANUS_API_KEY;

if (!API_KEY) {
  console.error("Error: MANUS_API_KEY not set");
  process.exit(1);
}

const action = process.argv[2];
const args = process.argv.slice(3);

async function request(endpoint, method = 'GET', data = null) {
  return new Promise((resolve, reject) => {
    const options = url.parse(`${API_BASE}${endpoint}`);
    options.method = method;
    options.headers = {
      'API_KEY': API_KEY,
      'Content-Type': 'application/json'
    };

    const req = https.request(options, (res) => {
      let body = '';
      res.on('data', (chunk) => body += chunk);
      res.on('end', () => {
        try {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve(JSON.parse(body));
          } else {
            reject(new Error(`API Error ${res.statusCode}: ${body}`));
          }
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on('error', (e) => reject(e));
    if (data) req.write(JSON.stringify(data));
    req.end();
  });
}

async function downloadFile(fileUrl, outputPath) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(outputPath);
    https.get(fileUrl, (response) => {
      response.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve(outputPath);
      });
    }).on('error', (err) => {
      fs.unlink(outputPath, () => {}); // Delete the file async. (But we don't check the result)
      reject(err);
    });
  });
}

async function main() {
  try {
    switch (action) {
      case 'create':
        const prompt = args[0];
        const profile = args[1] || 'manus-1.6';
        const task = await request('/tasks', 'POST', {
          prompt,
          agentProfile: profile,
          taskMode: 'agent',
          createShareableLink: false
        });
        console.log(JSON.stringify(task));
        break;

      case 'get':
        const taskIdGet = args[0];
        const taskGet = await request(`/tasks/${taskIdGet}`);
        console.log(JSON.stringify(taskGet, null, 2));
        break;

      case 'status':
        const taskIdStatus = args[0];
        const taskStatus = await request(`/tasks/${taskIdStatus}`);
        console.log(taskStatus.status || 'unknown');
        break;

      case 'wait':
        const taskIdWait = args[0];
        const timeout = parseInt(args[1] || '600', 10);
        let elapsed = 0;
        const interval = 10;

        while (elapsed < timeout) {
          const statusRes = await request(`/tasks/${taskIdWait}`);
          const status = statusRes.status || 'unknown';

          if (status === 'completed') {
            console.log('completed');
            process.exit(0);
          } else if (status === 'failed') {
            console.log('failed');
            process.exit(1);
          }

          await new Promise(resolve => setTimeout(resolve, interval * 1000));
          elapsed += interval;
          console.error(`waiting... (${elapsed}/${timeout} sec, status: ${status})`);
        }
        console.error('timeout');
        process.exit(1);
        break;

      case 'files':
        const taskIdFiles = args[0];
        const taskFiles = await request(`/tasks/${taskIdFiles}`);
        const files = (taskFiles.output || [])
          .flatMap(o => o.content || [])
          .filter(c => c.type === 'output_file');
        
        files.forEach(f => console.log(`${f.fileName}\t${f.fileUrl}`));
        break;

      case 'download':
        const taskIdDL = args[0];
        const outputDir = args[1] || '.';
        if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

        const taskDL = await request(`/tasks/${taskIdDL}`);
        const filesDL = (taskDL.output || [])
          .flatMap(o => o.content || [])
          .filter(c => c.type === 'output_file');

        for (const file of filesDL) {
          const safeName = file.fileName.replace(/[^a-zA-Z0-9._-]/g, '').substring(0, 100) || 'output_file';
          const dest = `${outputDir}/${safeName}`;
          console.error(`Downloading: ${safeName}`);
          await downloadFile(file.fileUrl, dest);
          console.log(dest);
        }
        break;

      case 'list':
        const tasks = await request('/tasks');
        console.log(JSON.stringify(tasks, null, 2));
        break;

      default:
        console.error("Usage: node manus.js <command> [args]");
        process.exit(1);
    }
  } catch (error) {
    console.error("Error:", error.message);
    process.exit(1);
  }
}

main();
