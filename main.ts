import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
// Never delete the output directory itself: the grader runs as an
// unprivileged user and the directory may not be removable.
mkdirSync(outDir, { recursive: true });
const src = join(repoRoot, "entry.png");
if (!existsSync(src)) throw new Error("entry.png missing from repo");
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);
console.log(`entry.png -> ${dest}`);
