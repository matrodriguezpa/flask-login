import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';
import Protected from './Protected';

function App() {
  const [token, setToken] = useState('');

  return (
    <div>
      <Register />
      <Login setToken={setToken} />
      <Protected token={token} />
    </div>
  );
}

export default App;
