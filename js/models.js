"use strict";

const BASE_URL = "http://localhost:5000/api/";


/*******************************************************************************
 * Cupcake instance 
 */

class Cupcake {
    /** Make instance of Cupcake from JSON object:
   *   - {cupcakeId, flavor, size, rating, image}
   */
    constructor({cupcakeId, flavor, size, rating, image}){
        this.cupcakeId = cupcakeId;
        this.flavor = flavor;
        this.size = size;
        this.rating = rating;
        this.image = image;
    }

}

/*******************************************************************************
 * List of cupcake instances
 */

class CupcakeList {
    constructor(cupcakes) {
        this.cupcakes = cupcakes;
    }
    // query the /cupcakes endpoint (no auth required)
    static async getCupcakes() {
        const response = await axios({
            url: `${BASE_URL}/cupcakes`, 
            method: "GET",
        });

    const cupcakes = response.data.cupcakes.map(cupcake => new Cupcake(cupcake));

    return new CupcakeList(cupcakes);
    }

    async addCupcake(cupcake) {

        cupcakeToJSON = JSON.stringify({
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image,
        });
    
        const response = await axios.post(`${BASE_URL}/cupcakes`, cupcakeToJSON);
          
    
        const newCupcake = new Cupcake(response.data.cupcake);
        
        // Possible update HERE 
        this.cupcakes.push(newCupcake);
    
        return newCupcake;
      }
}