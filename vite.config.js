import path from "path";
import { NodePackageImporter } from "sass";
import { fileURLToPath } from "url";
import { defineConfig } from "vite";

export default defineConfig({
  build: {
    outDir: "iati_sphinx_theme/static/css",
    lib: {
      entry: {
        css: path.resolve(__dirname, "styles/main.scss"),
      },
      formats: ["es"],
    },
    cssMinify: false,
  },
  css: {
    preprocessorOptions: {
      scss: {
        pkgImporter: new NodePackageImporter(),
      },
    },
  },
  resolve: {
    alias: {
      "@assets": fileURLToPath(
        new URL("./node_modules/iati-design-system/src/assets", import.meta.url)
      ),
    },
  },
});
