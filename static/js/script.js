document.addEventListener('DOMContentLoaded', function() {
    const password = document.getElementById('password');
    const requirements = {
        length: document.getElementById('length'),
        uppercase: document.getElementById('uppercase'),
        lowercase: document.getElementById('lowercase'),
        number: document.getElementById('number')
    };

    password.addEventListener('input', function() {
        const value = this.value;

        if (value.length >= 8) {
            requirements.length.classList.add('valid')
        } else {
            requirements.length.classList.remove('valid')
        }

        if (/[A-Z]/.test(value)) {
            requirements.uppercase.classList.add('valid')
        } else {
            requirements.uppercase.classList.remove('valid')
        }

        if (/[a-z]/.test(value)) {
            requirements.lowercase.classList.add('valid')
        } else {
            requirements.lowercase.classList.remove('valid')
        }

        if (/[0-9]/.test(value)) {
            requirements.number.classList.add('valid')
        } else {
            requirements.number.classList.remove('valid')
        }
    })
})

