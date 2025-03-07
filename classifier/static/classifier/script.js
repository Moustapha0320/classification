ocument.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[type='file']");
    const preview = document.createElement("img");
    preview.style.maxWidth = "300px";
    preview.style.marginTop = "10px";

    fileInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                document.body.appendChild(preview);
            }
            reader.readAsDataURL(file);
        }
    });
});
