import "./homepage.css";
import carrot from '../images/carrot.jpg';
import tomato from '../images/tomato.png';
import pepper from '../images/pepper.png';
import broccoli from '../images/broccoli.png';

import { useState, useCallback } from 'react'

function HomePage({ setVeganisedUrl }) {
  const [inputValue, setInputValue] = useState("")

  const handleSubmit = useCallback(() => {
    setVeganisedUrl(inputValue)
  }, [inputValue, setVeganisedUrl])

  return (
    <div className="grid-container">
      <div className="title-box">
        <h1>V For Green</h1>
        <h2>A veganiser for all your meat recipes</h2>
      </div>
      <div className="content-box">
        <p>Submit a recipe to Veganise:</p>
        <input onChange={e => setInputValue(e.target.value)} placeholder="https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe" type="text"/>
        <button className="submit-button" onClick={() => handleSubmit()}>Submit</button>
      </div>
      <img className="carrot wiggler" src={carrot} alt="#"/>
      <img className="tomato wiggler" src={tomato} alt="#"/>
      <img className="pepper wiggler" src={pepper} alt="#"/>
      <img className="broccoli wiggler" src={broccoli} alt="#"/>
    </div>
  );
}

export default HomePage;