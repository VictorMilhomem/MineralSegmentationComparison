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
    'num_images_train': 10000,
    'rotate': True,
    'flip': True,
    'max_epochs': 25,
    'patience': 10,
    'progress_threshold': 0.01,
    'lr_config': {'learning_rate': 0.001},
    'optimizer_config': {'type': 'Adam'}
}
