import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import HomePage from './homepage/homepage.js';
import VeganisedPage from './veganisedpage/veganisedpage.js'

const Router = () => {
    const [veganisedUrl, setVeganisedUrl] = useState('')

    switch(veganisedUrl) {
        case '':
            return <HomePage setVeganisedUrl={setVeganisedUrl}/>
        default:
            return <VeganisedPage veganisedUrl={veganisedUrl} />
    }
}

ReactDOM.render(
    <Router />,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
