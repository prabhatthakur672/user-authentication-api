# Request/Response Structure

## 1.`SendOTP` Endpoint
### URL: `/api/send-otp/`
### Method: POST

### Request Body Example:
<pre>
  <code id="clone-command">
    {
      "phone_number": "+911234567890"
    }
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>
### Response Examples:
-**1.Success Response:**
<pre>
  <code id="clone-command">
    {
    "message": "OTP sent successfully."
    }
</pre>
<button onclick="copyToClipboard('#clone-command')"></button>
- **Status:** `200 OK`
