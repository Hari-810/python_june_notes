// Base API URL
const API_URL = 'http://127.0.0.1:5000';

// Event listener for form submission
document.getElementById('create-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission behavior

    // Get input values from the form
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const email = document.getElementById('email').value;

    // Send a POST request to the /insert endpoint with the form data
    const response = await fetch(`${API_URL}/insert`, {
        method: 'POST', // HTTP method
        headers: {
            'Content-Type': 'application/json' // Content type is JSON
        },
        body: JSON.stringify({ name, age, email }) // Convert data to JSON string
    });

    // Parse the response from the server
    const result = await response.json();
    if (response.status === 201) {
        alert('Document inserted'); // Alert if insertion was successful
        fetchDocuments(); // Refresh the documents list
    } else {
        alert('Error inserting document: ' + result.error); // Alert if there was an error
    }
});

// Function to fetch and display all documents
async function fetchDocuments() {
    // Send a GET request to the /documents endpoint
    const response = await fetch(`${API_URL}/documents`);
    // Parse the response from the server
    const documents = await response.json();

    // Get the documents div to display the documents
    const documentsDiv = document.getElementById('documents');
    documentsDiv.innerHTML = ''; // Clear the div

    // Iterate over each document and create a div element for it
    documents.forEach(doc => {
        const docDiv = document.createElement('div');
        docDiv.className = 'document'; // Add class for styling
        docDiv.innerHTML = `
            <span>${doc.name} - ${doc.age} - ${doc.email}</span>
            <div>
                <button onclick="updateDocument('${doc._id}')">Update</button>
                <button onclick="deleteDocument('${doc._id}')">Delete</button>
            </div>
        `; // Add document details and buttons for update and delete
        documentsDiv.appendChild(docDiv); // Append the document div to the documents div
    });
}

// Function to update a document
async function updateDocument(id) {
    // Prompt the user for new values
    const name = prompt('Enter new name');
    const age = prompt('Enter new age');
    const email = prompt('Enter new email');

    // Send a PUT request to the /documents/:id endpoint with the new data
    const response = await fetch(`${API_URL}/documents/${id}`, {
        method: 'PUT', // HTTP method
        headers: {
            'Content-Type': 'application/json' // Content type is JSON
        },
        body: JSON.stringify({ name, age, email }) // Convert data to JSON string
    });

    // Parse the response from the server
    const result = await response.json();
    if (response.status === 200) {
        alert('Document updated'); // Alert if update was successful
        fetchDocuments(); // Refresh the documents list
    } else {
        alert('Error updating document: ' + result.error); // Alert if there was an error
    }
}

// Function to delete a document
async function deleteDocument(id) {
    // Send a DELETE request to the /documents/:id endpoint
    const response = await fetch(`${API_URL}/documents/${id}`, {
        method: 'DELETE' // HTTP method
    });

    // Parse the response from the server
    const result = await response.json();
    if (response.status === 200) {
        alert('Document deleted'); // Alert if deletion was successful
        fetchDocuments(); // Refresh the documents list
    } else {
        alert('Error deleting document: ' + result.error); // Alert if there was an error
    }
}

// Initial fetch to display documents when the page loads
fetchDocuments();
