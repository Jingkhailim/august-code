# Oracle & OCI Sample Scripts

This repo contains two standalone Python examples:

1. **Oracle Autonomous Database connection test** (`db_connect.py`)
2. **OCI Generative AI — Text Embedding demo** (`embed_text_demo.py`)

---

## 1. Oracle Autonomous Database Connection

Tests connectivity to an Oracle Autonomous Database (ADB) instance using the
[`python-oracledb`](https://oracle.github.io/python-oracledb/) driver.

### Setup

1. Follow the official quickstart for driver installation:
   https://www.oracle.com/database/technologies/appdev/python/quickstartpython.html
2. Install the driver:
   ```bash
   pip install oracledb
   ```
3. Set your credentials as environment variables (recommended) rather than
   hardcoding them in the script:
   ```bash
   export DB_USER="your_username"
   export DB_PASSWORD="your_password"
   ```
   and load them with `os.environ["DB_USER"]` / `os.environ["DB_PASSWORD"]`.

### Connection modes

- **THIN mode (default)** — no Oracle Client libraries required. Works out of
  the box with the `CONNECT_STRING` (TNS descriptor) shown in the script.
- **THICK mode** — uncomment `oracledb.init_oracle_client()` if you need
  features only available in Thick mode (e.g. certain older DB versions).
- **Wallet-based connection** — if you're using a downloaded wallet:
  - Comment out the inline `CONNECT_STRING` and instead set
    `CONNECT_STRING = "your_tns_alias"` (the alias from `tnsnames.ora`).
  - Pass `config_dir="/path/to/wallet_dir/"` to `create_pool()`.
  - For Thin mode on Python 3.13+, also supply `wallet_location` and
    `wallet_password`.

### Run

```bash
python db_connect.py
```

Expected output on success:
```
Connected successfully! Query result: 1
```

> **Note:** The script includes two connect-string variants (`_duck_medium`
> and `_duck_high`), corresponding to different ADB predefined database
> service levels (e.g. MEDIUM vs HIGH consumer groups). Use the one that
> matches your workload.

---

## 2. OCI Generative AI — Text Embedding Demo

Generates text embeddings using OCI's Generative AI service (Cohere
`embed-english-light-v3.0` model).

### Setup

1. Install the OCI SDK:
   ```bash
   pip install oci
   ```
2. Configure your OCI CLI/SDK config file (typically `~/.oci/config`), containing
   your tenancy OCID, user OCID, fingerprint, and private key path. See:
   https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
3. Update the script to point at your config file and profile:
   ```python
   config = oci.config.from_file("~/.oci/config", "DEFAULT")
   ```
   Avoid hardcoding an absolute Windows path or committing your config path
   into version control.
4. Set `compartment_id` to your own compartment OCID.

### Run

```bash
python embed_text_demo.py
```

The script embeds a small list of sample strings and prints, for each input,
the vector dimensionality and the first 10 values of its embedding.

---

## Security notes

Both scripts currently contain hardcoded identifiers (OCIDs, a connect
string, and what appears to be a leftover credential/token in a comment).
Before sharing or committing this code:

- Remove any hardcoded usernames, passwords, tokens, or API keys.
- Move secrets to environment variables, a `.env` file (git-ignored), or a
  secrets manager.
- Double-check comments for accidentally pasted credentials — comments are
  easy to overlook but still expose secrets if committed to a repo.
- OCIDs (compartment/tenancy IDs) aren't secret by themselves, but it's still
  good practice to keep them out of shared/public code and load them from
  config instead.
