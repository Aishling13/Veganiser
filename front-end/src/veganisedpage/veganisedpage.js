import './veganisedpage.css'

import { useState, useEffect } from 'react'

function VeganisedPage({ veganisedUrl }) {
  const [pageReady, setPageReady] = useState(false)

  useEffect(() => {
    const formData = new FormData();
    formData.append('url', veganisedUrl)

    fetch('http://localhost:5000/veganise', {
      method: 'POST',
      body: formData,
    })
    .then(res => res.text())
    .then(body => {
      setPageReady(true)
      const doc = document.getElementById('VeganisedPage').contentWindow.document;
      doc.open();
      doc.write(body);
      doc.close();
    })
    .catch(err => alert(err))
  }, [veganisedUrl])

  if (!pageReady) {
    return (
      <div className="loading-page">
        <div className="loading-group">
          <img className="loading-pepper" src='https://i.imgur.com/v2BrLKm.png' alt="#"/>
          <h2>Loading...</h2>
        </div>
      </div>
    )
  } else {
    return (
      <div>
        <iframe id="VeganisedPage" title="VeganisedPage" src="about:blank"/>
        <img className="carrot wiggler" src='https://i.imgur.com/GMdoFaB.png' alt="#"/>
        <img className="tomato wiggler" src='https://i.imgur.com/pLob3ZX.png' alt="#"/>
      </div>
    )
  }
}

export default VeganisedPage;