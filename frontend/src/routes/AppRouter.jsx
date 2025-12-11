import {Route, Routes} from "react-router-dom";


import Login from "../pages/authentication/Login.jsx";
import Register from "../pages/authentication/Register.jsx";
import AdminDashboard from "../pages/admin/AdminDashboard.jsx";
import VendorDashboard from "../pages/vendor/VendorDashboard.jsx";
import CustomerPage from "../pages/customer/CustomerPage.jsx";

export default function AppRouter() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/admin" element={<AdminDashboard />} />
            <Route path="/vendor" element={<VendorDashboard />} />
            <Route path="/customer" element={<CustomerPage />} />

            {/*protected routes to be added later*/}

        </Routes>
    )
}