/// Pages
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login"
import RegisterPage from "./pages/Register";
import HomePage from "./pages/Home";
import Dashboard from "./pages/Dashboard";
/// Authentication Required
import AuthenticationRequired from "./components/AuthenticationRequired";

///* CODE:

function App() {

  function Logout() {
    localStorage.clear();
    return <Navigate to="/" />;
  }

  function LogoutAndRegister() {
    localStorage.clear();
    return <RegisterPage />;
  }

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/register" element={<LogoutAndRegister />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard/>}/>
          {/*
          <Route path="*" element={<NotFound />} />
          */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;