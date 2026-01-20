let dashboardGenerated = false;

async function generateDashboard() {
    const data = document.getElementById("jsonInput").value;
    const prompt = document.getElementById("userPrompt").value;
    if (!data || !prompt) {
        alert("Please provide JSON data and a prompt.");
        return;
    }

    setGeneratingState(true);

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ data, prompt })
        });

        const result = await response.json();

        if (result.error) {
            alert(result.error);
            return;
        }

        const iframe = document.getElementById("preview");
        iframe.srcdoc = result.html;

        dashboardGenerated = true;

        const downloadBtn = document.getElementById("downloadBtn");
        downloadBtn.disabled = false;
        downloadBtn.classList.remove("bg-gray-400", "cursor-not-allowed");
        downloadBtn.classList.add("bg-blue-600", "hover:bg-blue-700");

    } catch (error) {
        alert("Something went wrong. Please try again.");
        console.error(error);
    } finally {
        setGeneratingState(false);
    }
}




function setGeneratingState(isGenerating) {
    const btn = document.getElementById("genBtn");

    if (isGenerating) {
        btn.innerText = "Generating...";
        btn.disabled = true;
        btn.classList.add("bg-gray-400", "cursor-not-allowed");
        btn.classList.remove("bg-blue-600", "hover:bg-blue-700");
    } else {
        btn.innerText = "Generate";
        btn.disabled = false;
        btn.classList.remove("bg-gray-400", "cursor-not-allowed");
        btn.classList.add("bg-blue-600", "hover:bg-blue-700");
    }
}


function downloadScreenshot() {
    if (document.getElementById("downloadBtn").disabled) {
    alert("Generate the dashboard first.");
    return;
}

    const iframe = document.getElementById("preview");
    const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;

    html2canvas(iframeDocument.body).then(canvas => {
        const link = document.createElement("a");
        link.download = "dashboard.png";
        link.href = canvas.toDataURL("image/png");
        link.click();
    });
}


