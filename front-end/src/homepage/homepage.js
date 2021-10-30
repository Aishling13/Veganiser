import "./homepage.css";

import { useState, useCallback } from 'react'

function HomePage({ setVeganisedUrl }) {
  const [inputValue, setInputValue] = useState("")

  const handleSubmit = useCallback(() => {
    setVeganisedUrl(inputValue)
  }, [inputValue, setVeganisedUrl])

  return (
    <div className="grid-container">
      <div className="title-box">
        <h1>Veganise It!</h1>
        <h2>A veganiser for all your favourite recipes</h2>
      </div>
      <div className="content-box">
        <p>Submit a recipe to Veganise:</p>
        <input onChange={e => setInputValue(e.target.value)} placeholder="https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe" type="text"/>
        <button className="submit-button" onClick={() => handleSubmit()}>Veganise!</button>
      </div>
      <img className="carrot wiggler" src='https://i.imgur.com/GMdoFaB.png' alt="#"/>
      <img className="tomato wiggler" src='https://i.imgur.com/pLob3ZX.png' alt="#"/>
      <img className="pepper wiggler" src='https://i.imgur.com/v2BrLKm.png' alt="#"/>
      <img className="broccoli wiggler" src='https://i.imgur.com/E9dGIC9.png' alt="#"/>
    </div>
  );
}

export default HomePage;