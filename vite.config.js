import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/python-new-project/',   // 🔥 MUST MATCH YOUR REPO NAME ON GITHUB
})
