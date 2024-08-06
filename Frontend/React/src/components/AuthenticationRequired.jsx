import { useNavigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "./api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "./constants";
import { useState, useEffect } from "react";

function AuthenticationRequired({ page }) {
    const [isAuthorized, setIsAuthorized] = useState(null); // State to track authorization status
    const navigate = useNavigate(); // Hook to navigate pages

    useEffect(() => {
        // Call the auth function when the component mounts
        auth().catch(() => setIsAuthorized(false));
    }, []);

    // Function to refresh the access token using the refresh token
    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN); // Get the refresh token from local storage
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            });
            if (res.status === 200) {
                // If the response is successful, update the access token
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true);
            } else {
                setIsAuthorized(false);
            }
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    };

    // Function to check the authentication status asynchronously
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN); // Get the access token from local storage
        if (!token) {
            setIsAuthorized(false);
            return;
        }
        const decoded = jwtDecode(token); // Decode the token to get its expiration time
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {
            // If the token has expired, attempt to refresh it
            await refreshToken();
        } else {
            setIsAuthorized(true); // If the token is still valid, authorize the user
        }
    };

    if (isAuthorized === null) {
        return <div>Loading...</div>; // Show a loading message while checking authentication
    }

    return isAuthorized ? page : navigate('/login'); // Render the page if authorized, otherwise navigate to login
}

export default AuthenticationRequired;
