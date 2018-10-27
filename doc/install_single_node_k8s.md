创建单节点 k8s 国内
=================
total root , copy paste support.

1 docker 安装

```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

2. 配置docker 加速
```bash
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://do7sudbb.mirror.aliyuncs.com"]
}
EOF
systemctl daemon-reload
systemctl enable docker.service
systemctl restart docker

```


2. 安装 kubeadm kubelet, kubectl --- 该脚本只适用 centos
```bash
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
        http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

# Set SELinux in permissive mode (effectively disabling it)
setenforce 0
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes

systemctl enable kubelet && systemctl start kubelet
```

3. linux configs
```bash
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system
systemctl stop firewalld && systemctl disable firewalld
setenforce 0
sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config && cat /etc/selinux/config 
swapoff -a  

```

4. 修改到国内 mirror 

注意 所有下文 本机ip 要填写正确。。。。.

```bash
cat <<EOF > ./config.yaml
apiVersion: kubeadm.k8s.io/v1alpha3
kind: ClusterConfiguration
kubernetesVersion: v1.12.1
apiServerCertSANs:
- "0.0.0.0"
api:
  advertiseAddress: 《本机ip》
etcd:
  endpoints:
  - https://《本机ip》:2379
networking:
  podSubnet: "10.244.0.0/16"
imageRepository: "registry.cn-hangzhou.aliyuncs.com/google_containers"
EOF

```

这里要手动修改。。。
```bash
vim /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
```

为 `ExecStart`的最后添加 参数： `--pod_infra_container_image=registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1`
最后结果形如：
```bash
# Note: This dropin only works with kubeadm and kubelet v1.11+
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
# This is a file that "kubeadm init" and "kubeadm join" generates at runtime, populating the KUBELET_KUBEADM_ARGS variable dynamically
EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
# This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably, the user should use
# the .NodeRegistration.KubeletExtraArgs object in the configuration files instead. KUBELET_EXTRA_ARGS should be sourced from this file.
EnvironmentFile=-/etc/sysconfig/kubelet
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS --pod_infra_container_image=registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1
```

5. 初始化集群
```bash
kubeadm init --config config.yaml
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-
kubectl get pods --all-namespaces

```
