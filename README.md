# Make an environment

```
conda create -n omnibench
conda activate omnibench
conda install python=3.9.10 pip -y
pip install -U outerbounds
```

# Configure Outerbounds platform access
Go [here](https://ui.dev-content.outerbounds.xyz/) and find your setup key!

# Run flows
```
python flow.py --environment=pypi run --with kubernetes
```