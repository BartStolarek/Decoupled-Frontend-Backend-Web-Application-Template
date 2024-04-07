import { useEffect } from "react";
import { useAuth } from "@/contexts/AuthContext";
import { useAlert } from "@/contexts/AlertContext";

type Role = "Administrator" | "User";

const useRequireAuth = (requiredRole: Role) => {
  const { isAuthenticated, loading } = useAuth();
  const { showAlert } = useAlert();

  useEffect(() => {
    // This effect should run after loading is complete and if the user's
    // authentication status is confirmed to avoid unnecessary checks.
    if (!loading) {
      const role = localStorage.getItem("user_role");
      // Assuming role validation is based on the presence of a 'user_role' key in localStorage
      // It's recommended to use a more secure method for production applications.

      // Check if the user is not authenticated or does not have the required role
      if (!isAuthenticated || role !== requiredRole) {
        const alertMessage = requiredRole === "Administrator"
          ? "You are not authorized to access this page. Please login with an Administrator account."
          : "You are not authorized to access this page. Please login.";

        // Show an alert and handle redirection after a timeout
        showAlert("Unauthorized", alertMessage, "error", "/login", 20000);
      }
    }
  }, [isAuthenticated, loading, showAlert, requiredRole]);

  // The hook returns only isAuthenticated and loading states for now.
  return { isAuthenticated, loading };
};

export default useRequireAuth;
