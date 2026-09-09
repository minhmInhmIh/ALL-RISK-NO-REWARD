import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Join from './join_page/join_page.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Join />
  </StrictMode>,
)
