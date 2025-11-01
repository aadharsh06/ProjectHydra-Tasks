
---

### **Task 0 – Environment Setup & GitHub Push**

**Objective:**
so we need to understand what are going, for that we need to make sure our setup works in the first place
Prepare your local environment for Kubernetes workflow,
ensure you can deploy and monitor a basic cluster later,
verify GitHub access for version control.

---

#### **Step 1. Install Required Tools**

Install and verify the following tools:

| Tool                | Purpose                  | Command to verify                   |
| ------------------- | ------------------------ | ----------------------------------- |
| Docker / containerd | Container runtime        | `docker --version`                  |
| kubectl             | Kubernetes CLI           | `kubectl version --client`          |
| minikube / kind     | Local Kubernetes cluster | `minikube version` / `kind version` |
| helm                | Package manager for K8s  | `helm version`                      |
| git                 | Version control          | `git --version`                     |

>  put a screenshot of terminal showing all 5 tools installed and working.

---

#### **Step 2. Create a Sample App**

Make a simple **Node.js or Python app** (your choice) that:

* Has a single `/health` endpoint returning `"OK"`.
* Includes a `Dockerfile` to containerize it.
* Has a `README.md` explaining setup and run steps.

> **Deliverable:**
> A working container image that runs locally (`docker run ...` shows app working on localhost).

---

#### **Step 3. Push to GitHub**

1. Create a new **public repo** under your account, e.g. `k8s-monitoring-lab`.
2. Add:

   ```
   /app
   /Dockerfile
   /README.md
   ```
3. Commit with message:

   ```
   Initial commit - Task 0 setup complete
   ```
4. Push to GitHub and share repo link.

> **Deliverable:** GitHub repository link.

---

>  This is gonna prepare you for Task 1 (Kubernetes cluster setup and monitoring integration).

---

