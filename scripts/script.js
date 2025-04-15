const sentimentElement = document.getElementById('sentiment');

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const text = document.getElementById('text').value;
    sentimentElement.textContent = 'Classifying...';

    // Send data to server using fetch API (assuming server-side script)
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify({ text }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        sentimentElement.textContent = `Sentiment: ${data.sentiment}`;
    })
    .catch(error => {
        console.error('Error:', error);
        sentimentElement.textContent = 'An error occurred.';
    });
});
