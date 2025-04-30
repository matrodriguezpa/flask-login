// src/App.js
import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';
import Protected from './Protected';

function App() {
  // 1. Token lives here now
  const [token, setToken] = useState('');

  return (
    <div>
      <Register />
      {/* 2. Pass the setter down so Login can update parent state */}
      <Login setToken={setToken} />
      {/* 3. Only show Protected if token is truthy */}
      {token && <Protected token={token} />}
    </div>
  );
}

export default App;
