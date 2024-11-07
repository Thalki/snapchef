// app.js

// Adding items to pantry and shopping list dynamically
document.addEventListener('DOMContentLoaded', function () {
    // Add pantry item
    document.querySelector('#add-pantry-item').addEventListener('click', function () {
        const newItem = document.querySelector('#pantry-input').value;
        if (newItem) {
            const list = document.querySelector('#pantry-list');
            const itemElement = document.createElement('li');
            itemElement.textContent = newItem;
            list.appendChild(itemElement);

            // Clear input after adding
            document.querySelector('#pantry-input').value = '';
        }
    });

    // Add shopping list item
    document.querySelector('#add-shopping-item').addEventListener('click', function () {
        const newItem = document.querySelector('#shopping-input').value;
        if (newItem) {
            const list = document.querySelector('#shopping-list');
            const itemElement = document.createElement('li');
            itemElement.textContent = newItem;
            list.appendChild(itemElement);

            // Clear input after adding
            document.querySelector('#shopping-input').value = '';
        }
    });

    // Remove items from pantry or shopping list on click
    document.querySelectorAll('.item-list').forEach(list => {
        list.addEventListener('click', function (event) {
            if (event.target.tagName === 'LI') {
                event.target.remove();
            }
        });
    });
});
