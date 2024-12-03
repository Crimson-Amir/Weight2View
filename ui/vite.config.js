import path from "path"
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default {
    plugins: [vue()],
    resolve: {
        alias: {
          vue: 'vue/dist/vue.esm-bundler.js',
          "@": path.resolve(__dirname, "./src")
        }
    },
    server: {
        open: true
    }
}