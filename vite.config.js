import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import svgLoader from "vite-svg-loader";
import path from "path";

export default defineConfig({
  plugins: [vue(), svgLoader()],
  build: {
    lib: {
      entry: path.resolve(__dirname, "/lib/index.js"),
      name: "IkkowyIconsVue",
      fileName: "icons-vue"
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue"
        }
      }
    }
  }
});
