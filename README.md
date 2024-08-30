# Request/Response Structure

## 1. `SendOTP` Endpoint

### URL: `/api/send-otp/`
### Method: `POST`

### Request Body Example:
<pre>
  <code id="send-otp-request">
    {
      "phone_number": "+911234567890"
    }
  </code>
</pre>
<button onclick="copyToClipboard('#send-otp-request')"></button>

### Response Examples:

- **1. Success Response:**
<pre>
  <code id="send-otp-success">
    {
      "message": "OTP sent successfully."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#send-otp-success')"></button>
Status: `200 OK`


- **2. Error Response (Phone number missing):**
<pre>
  <code id="send-otp-error-missing">
    {
      "error": "Phone number is required."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#send-otp-error-missing')">Copy</button>
- **Status:** `400 Bad Request`

- **3. Error Response (Phone number length incorrect):**
<pre>
  <code id="send-otp-error-length">
    {
      "error": "Phone number should have country code and 10 digits."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#send-otp-error-length')">Copy</button>
- **Status:** `400 Bad Request`

- **4. Error Response (Twilio Error):**
<pre>
  <code id="send-otp-error-twilio">
    {
      "error": "Detailed Twilio error message."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#send-otp-error-twilio')">Copy</button>
- **Status:** `500 Internal Server Error`

---

## 2. `VerifyAndAuthenticateUser` Endpoint

### URL: `/api/verify-otp/`
### Method: `POST`

### Request Body Example:
<pre>
  <code id="verify-otp-request">
    {
      "phone_number": "+911234567890",
      "otp": "1234"
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-request')">Copy</button>

### Response Examples:

- **1. Success Response (When OTP is verified and user is authenticated):**
<pre>
  <code id="verify-otp-success">
    {
      "message": "OTP verified successfully.",
      "token": "your_jwt_token_here"
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-success')">Copy</button>
- **Status:** `200 OK`

- **2. Error Response (Phone number or OTP missing):**
<pre>
  <code id="verify-otp-error-missing">
    {
      "error": "Phone number and OTP are required."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-error-missing')">Copy</button>
- **Status:** `400 Bad Request`

- **3. Error Response (Phone number length incorrect):**
<pre>
  <code id="verify-otp-error-length">
    {
      "error": "Phone number should have country code and 10 digits."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-error-length')">Copy</button>
- **Status:** `400 Bad Request`

- **4. Error Response (OTP length incorrect):**
<pre>
  <code id="verify-otp-error-otp-length">
    {
      "error": "OTP should've 4 digits."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-error-otp-length')">Copy</button>
- **Status:** `400 Bad Request`

- **5. Error Response (Invalid Credentials):**
<pre>
  <code id="verify-otp-error-invalid">
    {
      "error": "Invalid Credentials."
    }
  </code>
</pre>
<button onclick="copyToClipboard('#verify-otp-error-invalid')">Copy</button>
- **Status:** `400 Bad Request`
