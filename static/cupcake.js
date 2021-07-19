"use strict"

const $cupcakes = $(".cupcakes-list");
const $form = $("#new-cupcake-form");

/** Start */
async function start() {
    let response = await axios.get("/api/cupcakes");
    let cupcakes = response.data.cupcakes;

    displayCupcakes(cupcakes);
}

/** Display cupcakes list */
function displayCupcakes(cupcakes) {
    $cupcakes.empty();
    for (let cupcake of cupcakes) {
        $cupcakes.append(`<li>${cupcake.flavor}</li>`);
    }
}

/** Handle form submit: submit to API, focus on input. */
async function handleFormSubmit(evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();

    const response = await axios({
        url: "/api/cupcakes",
        method: "POST",
        data: { cupcake: {
            flavor,
            size,
            rating,
            image
        }}
    });  
    
    new_cupcake = response.data.cupcake;
    
    $cupcakes.append(`<li>${new_cupcake.flavor}</li>`);
}

$form.on("submit", handleFormSubmit);

start();
// function showCupcake(cupcake) {
//     $cupcakes.append(<li></li>cupcake)
// }


// async function submitCupcakeToAPI(cupcake) {
//     const response = await axios({
//         url: "/api/cupcakes",
//         method: "POST"
//     });

//     const { result } = response.data;
// }
