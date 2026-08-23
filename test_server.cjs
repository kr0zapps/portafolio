const express = require('express');
const path = require('path');
const app = express();

app.use('/portafolio', express.static(path.join(__dirname, 'dist')));
app.get('/', (req, res) => res.redirect('/portafolio/'));

app.listen(4321, () => {
    console.log('Server running on http://localhost:4321/portafolio/');
});
