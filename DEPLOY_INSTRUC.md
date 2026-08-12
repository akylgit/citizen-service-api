# Citizen Service API — GitOps

## Архитектура

```text
GitHub → Argo CD → Helm → Kubernetes
```

Argo CD отслеживает GitHub-репозиторий и разворачивает Helm chart в Kubernetes.

## Helm Chart

Основной путь:

```text
helm/citizen-service-api/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── configmap.yaml
    ├── deployment.yaml
    └── service.yaml
```

## Argo CD

Application:

```text
citizen-service-api
```

Repository:

```text
https://github.com/akylgit/citizen-service-api.git
```

Path:

```text
helm/citizen-service-api
```

Проверка:

```bash
kubectl get application citizen-service-api -n argocd
```

Ожидаемый статус:

```text
Synced   Healthy
```

## ConfigMap Rollout

Для автоматического rollout при изменении ConfigMap используется checksum:

```yaml
checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
```

Изменение версии в `values.yaml`:

```yaml
APP_VERSION: "2.0"
```

приводит к изменению checksum и автоматическому обновлению Pods.

## Проверка приложения

```bash
kubectl get pods
kubectl get svc
```

Health check:

```bash
curl http://<URL>/health
```

Результат:

```json
{"status":"healthy"}
```

Текущая версия:

```text
2.0
```

## Изменение и deployment

```bash
git add .
git commit -m "Update application"
git push github main
```

После изменения Git Argo CD синхронизирует Kubernetes deployment.

