const submitBtn = document.querySelector(".submit-btn");

submitBtn.addEventListener('click', () => {
    const formData = new FormData(form);
    const object = {};
    formData.forEach((value, key) => {
        object[key] = value;
    });
    const json = JSON.stringify(object);
    console.log(json)

    fetch('http://localhost:8000/novo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    })
    .then(response => response.json())
    .then(data => {
        console.log('API response:', data);
        // Process the API response as needed
    })
    .catch(error => {
        console.error('API request failed:', error);
        // Handle the error
    });
});

