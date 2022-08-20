# Model parameters
# Moment arms adapted from OpenSim gait model (LowerLimb2015)
# Model strength and dimensions consistent with a 170cm tall, 75 kg male 
# Model pose (degrees): lumbar_extension = -15; pelvic_tilt = -20;
#                       hip_flexion = 45; knee_flexion = 45; 
#                       ankle_flexion = 20; all other angles 0
# Model modifications:
#  (1) talus, calcaneus, and toes segment combined into one foot
#      segment; mass and center of mass adjusted accordingly
#  (2) ignored mass of the patella (this is small, and its kinematics
#      w.r.t. knee flexion angle are complex; simpler to ingore for now)
#  (3) torso, humerus r/l, ulna r/l, radius r/l, hand r/l combined into
#      one segment; mass and center of mass adjusted accordingly
#  (4) when computing static equations (sum F, sum M on full body), only
#      used total HAT segment mass and total pelvis mass, and double femur,
#      tibia, foot segment masses since we're analyzing a planar system and 
#      lumping both legs into one
#  (5) T_max represents double the maximum isometric muscle force of each
#      muscle, again since we're analyzing a planar model and lumping both
#      legs into one.
# Statics equations for this model and pose calculated using MotionGenesis

# Muscle names, if you're interested
muscle_names = ["adductor_brevis"; "adductor_longus"; "addductor_magnus_distal"; "adductor_magnus_ischial"; "adductor_magnus_middle"; "adductor_magnus_proximal"; "biceps_femoris_long_head"; "biceps_femoris_short_head"; "extensor_digitorum_longus"; "ext_hallucis_longus"; "flexor_digitorum_longus"; "flexor_hallucis_longus"; "gastrocnemius_lateralis"; "gastrocnemius_medialis"; "gluteus_maximus_1"; "gluteus_maximus_2"; "gluteus_maximus_3"; "gluteus_medius_1"; "gluteus_medius_2"; "gluteus_medius_3"; "gluteus_minimus_1"; "gluteus_minimus_2"; "gluteus_minimus_3"; "gracilis"; "iliacus"; "peroneus_brevis"; "peroneus_longus"; "piriformis"; "psoas"; "rectus_femoris"; "sartorius"; "semimembranosus"; "semitendinosus"; "soleus"; "tensor_fascia_latae"; "tibilais_anterior"; "tibialis_posterior"; "vastus_intermedius"; "vastus_lateralis"; "vastus_medialis"; ]; 

# Number of muscles
n_musc = length(muscle_names);

# Muscle moment arms (meters)
momentArm_hipFlexion = [0.0159, 0.0288, -0.0499, -0.0611, -0.0292, 0.00426, -0.0618, 0, 0, 0, 0, 0, 0, 0, -0.0427, -0.0479, -0.0674, -0.00354, -0.0149, -0.0216, 0.00326, -0.00045, -0.0060, -0.0278, 0.0400, 0, 0, -0.0104, 0.0309, 0.0508, 0.0645, -0.0550, -0.0667, 0, 0.0632, 0, 0, 0, 0, 0 ]; 
momentArm_kneeFlexion = [0, 0, 0, 0, 0, 0, 0.0360, 0.0343, 0, 0, 0, 0, 0.0255, 0.0260, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0438, 0, 0, 0, 0, 0, -0.0426, 0.0322, 0.0459, 0.0547, 0, -0.0119, 0, 0, -0.0375, -0.0374, -0.0356 ]; 
momentArm_kneeExtension = -momentArm_kneeFlexion;
momentArm_ankleFlexion = [0, 0, 0, 0, 0, 0, 0, 0, 0.0371, 0.0402, -0.00426, -0.00969, -0.0381, -0.0380, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.00432, -0.00727, 0, 0, 0, 0, 0, 0, -0.0342, 0, 0.0440, -0.00571, 0, 0, 0 ]; 

# Muscle maximum tension (Newtons)
T_max = 2*[281.109, 361.109, 292.068, 294.468, 258.369, 207.336, 645.666, 270.353, 200.276, 110.346, 169.324, 376.934, 747.052, 1441.340, 404.915, 572.345, 383.648, 523.736, 339.662, 376.852, 184.053, 196.060, 212.610, 136.707, 435.225, 254.569, 496.089, 507.897, 692.290, 775.704, 124.665, 990.884, 283.813, 2791.850, 130.609, 403.693, 741.153, 849.744, 2497.050, 1268.760 ];

# Coefficient matrices for statics equations (SI units)
# Eqn (1): moment balance about ankle joint center for foot segment
# Eqn (2): moment balance about knee joint center for shank and foot segments
# Eqn (3): moment balance about hip joint center for thigh, shank, and foot segments
# Eqn (4): force balance in horizontal direction for full body system
# Eqn (5): force balance in vertical direction for full body system
# Eqn (6): moment balance about pelvis origin for full body system

A_musc = [ momentArm_ankleFlexion'
           momentArm_kneeExtension'
           momentArm_hipFlexion'
           zeros(1,length(T_max))
           zeros(1,length(T_max))
           zeros(1,length(T_max)) ];

A_toe = [ [0.0439500 0.22003000]
          [0.4164068 0.07382502]
          [0.7895632 0.23890430]
          [1.0       0.0       ]
          [0.0       1.0       ]
          [0.8440721 0.15917700] ];


A_heel = [ [0.0439500 -0.06997000]
           [0.4164068 -0.21617500]
           [0.7895632 -0.05109567]
           [1.0       0.0        ]
           [0.0       1.0        ]
           [0.8440721 -0.130823  ] ];

A_push = [ [0 0]
           [0 0]
           [0 0]
           [1 0]
           [0 1]
           [0 0] ];

b = [   1.9560426
      - 7.182712
       23.0106000
        0.0      
      737.3648000
       15.251638 ];

# Coefficient of static friction
mu = 0.7;
