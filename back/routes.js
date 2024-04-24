let lastVisited = "Gryffindor";

router.get('/iot/lastVisited', (req, res) => {
  return res.json({ lastVisited: lastVisited })
})

router.post('/iot/lastVisited', (req, res) => {
  lastVisited = req.body.lastVisited
  return res.json({ lastVisited: lastVisited })
})
