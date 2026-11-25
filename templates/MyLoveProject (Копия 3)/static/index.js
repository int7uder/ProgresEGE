const holdText = document.getElementById("holdText");
const finalButton = document.getElementById("finalButton");
const finalPage = document.getElementById("finalPage");
const message = document.getElementById("message");
const continueButton = document.getElementById("continueButton");
const bow = document.getElementById("bow");
const flowers = document.getElementById("flowers");
const memories = document.getElementById("memories");

let holdTimer = null;
let exploded = false;
let isHolding = false;


/* ==================== */
/* НАЖАТИЕ НА БАНТ */
/* ==================== */

bow.addEventListener("pointerdown", (event) => {
    if (exploded || isHolding) {
        return;
    }

    event.preventDefault();

    isHolding = true;

    bow.setPointerCapture(event.pointerId);

    bow.classList.add("shaking");

    holdTimer = setTimeout(() => {
        explode();
    }, 1500);
});


/* ==================== */
/* ОТПУСКАНИЕ */
/* ==================== */

function stopHolding() {
    if (!isHolding || exploded) {
        return;
    }

    isHolding = false;

    clearTimeout(holdTimer);
    holdTimer = null;

    bow.classList.remove("shaking");
}


bow.addEventListener("pointerup", stopHolding);

bow.addEventListener("pointercancel", stopHolding);


/* ==================== */
/* ВЗРЫВ */
/* ==================== */

function explode() {
    exploded = true;
    isHolding = false;

    clearTimeout(holdTimer);
    holdTimer = null;

    bow.classList.remove("shaking");
    bow.style.display = "none";


    const flowerElements = flowers.querySelectorAll("span");


    flowerElements.forEach((flower) => {

        const x = (Math.random() - 0.5) * 800;
        const y = (Math.random() - 0.5) * 600;
        const rotation = (Math.random() - 0.5) * 720;


        flower.style.setProperty(
            "--x",
            `${x}px`
        );

        flower.style.setProperty(
            "--y",
            `${y}px`
        );

        flower.style.setProperty(
            "--rotation",
            `${rotation}deg`
        );
    });


    flowers.classList.add("exploding");


    setTimeout(() => {
        message.classList.add("show");
    }, 1200);
}


/* ==================== */
/* КНОПКА "ДАЛЬШЕ" */
/* ==================== */

continueButton.addEventListener("click", () => {
    message.classList.remove("show");

    memories.classList.add("show");

    setTimeout(() => {
        memories.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 100);
});

finalButton.addEventListener("click", () => {
    memories.classList.add("hide-content");

    setTimeout(() => {
        finalPage.classList.add("show");

        finalPage.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 700);
});