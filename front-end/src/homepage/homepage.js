import "./homepage.css";
import carrot from '../images/carrot.jpg';
import tomato from '../images/tomato.png';
import pepper from '../images/pepper.png';
import broccoli from '../images/broccoli.png';

function HomePage() {
  return (
    <div className="grid-container">
      <h1>Veganise IT!!</h1>
      <div className="content-box">
        <p>Recipe to Veganise:</p><input/>
        <button className="submit-button">Submit</button>
      </div>
      <img className="carrot" src={carrot} alt="cartoon carrot"/>
      <img className="tomato" src={tomato} alt="cartoon tomato"/>
      <img className="pepper" src={pepper} alt="cartoon pepper"/>
      <img className="broccoli" src={broccoli} alt="cartoon broccoli"/>
    </div>
  );
}

export default HomePage;