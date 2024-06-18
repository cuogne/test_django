document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('personForm').addEventListener('submit', function(event) {
        alert('Form has been submitted successfully!');
    });

    document.querySelectorAll('.delete-form').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this entry?')) {
                event.preventDefault();
            }
        });
    });
});

const toggleButton = document.getElementById('togglePersonList');
const personList = document.querySelector('.person-list');

toggleButton.addEventListener('click', function() {
    // check status of personList
    if (personList.style.display === 'none') {
        personList.style.display = 'block';
    } else {
        personList.style.display = 'none';
    }
});
