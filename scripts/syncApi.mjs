import path from "path";
import { generateApi } from "swagger-typescript-api";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const inputPath = path.join(__dirname, "../openapi.json");
const outputPath = path.join(__dirname, "../src/server/api");

generateApi({
  input: inputPath,
  httpClientType: "fetch",
  generateRouteTypes: true,
  generateResponses: true,
  name: "generated.ts",
  output: outputPath,
  silent: true,
})
  .then((res) => {
    console.log("Generated data science api");
  })
  .catch((err) => {
    console.error("Error generating data science api", err);
  })
  .finally(process.exit);
