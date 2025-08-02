import { useEffect, useState } from 'react'

function App() {
  const [msg, setMsg] = useState<string>('')

  useEffect(() => {
    fetch('http://localhost:5173/api/hello')
      .then(res => res.json())
      .then(data => setMsg(data.message))
  }, [])

  return (
    <div>
      <h1>OdontoCare</h1>
      <p>{msg}</p>
    </div>
  )
}

export default App