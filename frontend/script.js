document.getElementById("convertBtn").addEventListener("click", async () => {
    const imageFile = document.getElementById("imageInput").files[0];
    if (!imageFile) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("image", imageFile);

    try {
        const response = await fetch("http://localhost:5000/convert", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Failed to process image");
        }

        const data = await response.json();

        // Utility function to clean response
        const cleanCode = (code) => {
            if (!code) return "";
            return code
                .replace(/```html/g, "")   // remove ```html
                .replace(/```css/g, "")    // remove ```css
                .replace(/```/g, "")       // remove remaining ```
                .trim();
        };

        document.getElementById("htmlOutput").value = cleanCode(data.html) || "No HTML generated.";
        document.getElementById("cssOutput").value = cleanCode(data.css) || "No CSS generated.";
    } catch (error) {
        console.error(error);
        alert("Error converting image.");
    }
});
