const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = 3000;

// Allow serving static files (HTML/CSS/JS)
app.use(express.static(path.join(__dirname, 'public')));

app.get('/fetch-user', async (req, res) => {
    const userId = req.query.userId;

    if (!userId) {
        return res.status(400).send({ error: 'User ID is required' });
    }

    try {
        const response = await axios.get(`http://127.0.0.1:5000/user/${userId}`);
        res.send(response.data);
    } catch (error) {
        if (error.response && error.response.data) {
            res.status(error.response.status).send(error.response.data);
        } else {
            res.status(500).send({ error: 'Failed to fetch user data' });
        }
    }
});

app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
});
