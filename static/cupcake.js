"use strict"

const $cupcakes = $(".cupcakes-list");
const $form = $("#new-cupcake-form");

/** Start */
async function start() {
    let response = await axios.get("/api/cupcakes");
    let cupcakes = response.data.cupcakes;

    displayCupcakes(cupcakes);
}

/** Get Cupcakes function */

/** Generate cupcake HTML 
 * returns jquery of cupcake
*/
function generateCupcake(cupcake) {
    return ` 
        <div data-cupcake-id=${cupcake.id} class="col-4">
            <li>
            Flavor: ${cupcake.flavor} | Size: ${cupcake.size} | Rating: ${cupcake.rating}
            </li>
            <img class="Cupcake-img" src="${cupcake.image}" alt="No image provided" width="200px">
        </div>
   `;
}

/** Display cupcakes list */
function displayCupcakes(cupcakes) {
    $cupcakes.empty();
    console.log(cupcakes)
    for (let cupcake of cupcakes) {
        $cupcakes.append(generateCupcake(cupcake));
    }
}

/** Handle form submit: submit to API, focus on input. */
async function handleFormSubmit(evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();
    
    const response = await axios.post(
        "http://localhost:5000/api/cupcakes",
        {
            flavor,
            size,
            rating,
            image
        }
    );  
    // const response = await axios.post({
    //     url: "/api/cupcakes",
    //     data: {
    //         flavor,
    //         size,
    //         rating,
    //         image
    //     }
    // });  
    
    let new_cupcake = response.data.cupcake;
    console.log("made it pasttt", new_cupcake);
    $cupcakes.append(generateCupcake(cupcake));
    $form.trigger("reset");
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
