
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/login', (req, res) => {
  res.redirect('http://localhost:8501/?token=123456')
})

app.get('/verify', (req, res) => {
  console.log('verifying...', req.query)
  try {
    if (req.query?.token === '123456')
      res.send('OK')
    else
      res.status(403).send('ERR')
  } catch (e) {
    console.log(e.toString())
    res.status(500).send('ERR')
  }
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
