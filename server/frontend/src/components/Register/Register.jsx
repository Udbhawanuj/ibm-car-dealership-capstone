import React, { useState } from "react";
import "./Register.css";

export default function Register() {
  const [form, setForm] = useState({
    userName: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });
  const [message, setMessage] = useState("");

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const submitRegistration = async (event) => {
    event.preventDefault();
    setMessage("Creating your account...");
    try {
      const response = await fetch("/djangoapp/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(form),
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.message || result.error || "Registration failed");
      setMessage(`Welcome, ${result.userName}. Your account is ready.`);
      window.location.assign("/");
    } catch (error) {
      setMessage(error.message);
    }
  };

  return (
    <main className="register-page">
      <section className="register-card">
        <p className="register-eyebrow">JOIN THE COMMUNITY</p>
        <h1>Sign Up</h1>
        <p>Create an account to publish verified dealership reviews.</p>
        <form onSubmit={submitRegistration}>
          <label>
            Username
            <input name="userName" value={form.userName} onChange={updateField} required />
          </label>
          <label>
            First Name
            <input name="firstName" value={form.firstName} onChange={updateField} required />
          </label>
          <label>
            Last Name
            <input name="lastName" value={form.lastName} onChange={updateField} required />
          </label>
          <label>
            Email
            <input name="email" type="email" value={form.email} onChange={updateField} required />
          </label>
          <label className="full-width">
            Password
            <input name="password" type="password" value={form.password} onChange={updateField} minLength={8} required />
          </label>
          <button className="register-button full-width" type="submit">Register</button>
        </form>
        {message && <div role="status" className="register-message">{message}</div>}
      </section>
    </main>
  );
}
