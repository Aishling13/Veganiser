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
    return <>Loading</>
  } else {
    return (
      <div>
        <iframe id="VeganisedPage" title="VeganisedPage" src="about:blank"/>
      </div>
    )
  }
}

export default VeganisedPage;