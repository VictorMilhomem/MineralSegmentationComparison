NO_DOMAIN_ADAPTATION_CONFIG = [
    {
        'run_training': True,
        'dataset': 'Cu',
    }
]


NO_DOMAIN_ADAPTATION_GLOBAL_PARAMS = {
    'patch_size': 256,
    'channels': 1,
    'num_class': 2,
    'skip_conn': True,
    'num_runs': 5,
    'batch_size': 2,
    'val_fraction': 0.1,
    'num_images_train': 2808,
    'rotate': True,
    'flip': True,
    'max_epochs': 25,
    'patience': 10,
    'progress_threshold': 0.01,
    'lr_config': {
        'name': 'exp',  
        'lr0': 0.001,  
        'warmup': 0.1,  
        'alpha': 0.01,  
        'beta': 0.5   
    },
    'optimizer_config': {'name': 'adam'}
}
