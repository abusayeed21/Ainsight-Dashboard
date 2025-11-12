import React, { useEffect, useState } from 'react'
import Dashboard from './components/Dashboard'
import axios from 'axios'

const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:8000/api'

export default function App(){
  const [status, setStatus] = useState('starting')
  useEffect(()=>{
    axios.get(`${API_BASE}/metrics/health`).then(()=>setStatus('ok')).catch(()=>setStatus('down'))
  },[])
  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <header className="mb-6">
        <h1 className="text-3xl font-bold">AINSIGHT</h1>
        <p className="text-sm opacity-80">AI-Powered Linux Server Dashboard</p>
      </header>
      <main>
        {status === 'ok' ? <Dashboard apiBase={API_BASE} /> : <div>Backend not reachable ({status})</div>}
      </main>
    </div>
  )
}
