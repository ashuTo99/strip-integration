import React from "react";
import { Route ,Routes, BrowserRouter as Router} from 'react-router-dom';
import HomePage from "./homePage";



const App = () => {
  return (
<>

<Router>
<Routes>
  <Route path="/" element={<HomePage/>}/>
</Routes>
  </Router>
</>
  )

}

export default App;