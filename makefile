APP_NAME ?= magiclens
VERSION ?= 0.0.1
IMAGE_TAG = $(APP_NAME):$(VERSION)
TAR_FILE = $(APP_NAME).tar

# Ambiente padrão (dev)
ENV ?= dev
KUSTOMIZE_DIR = k8s/overlays/$(ENV)

.PHONY: build save import deploy clean

## 🔧 Builda a imagem local com Podman
build:
	podman build -t $(IMAGE_TAG) .

## 📦 Salva a imagem como .tar
save: build
	podman save -o $(TAR_FILE) $(IMAGE_TAG)

## 📥 Importa no containerd do K3s
import: save
	sudo ctr -n k8s.io images import $(TAR_FILE)

## 🚀 Aplica usando kustomize
deploy: import
	kubectl apply -k $(KUSTOMIZE_DIR)
	@echo "✅ Deploy realizado no ambiente '$(ENV)'"

## 🧹 Limpa o tar
clean:
	rm -f $(TAR_FILE)
	podman rmi -f $(IMAGE_TAG)