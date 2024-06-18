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
